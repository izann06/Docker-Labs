# Creo el espacio organizativo donde vivirán mis contenedores
resource "aws_ecs_cluster" "homelab_cluster" { # Recurso tipo cluster de ECS
  name = "homelab-cluster"                     # Nombre del clúster
}


# Defino la tarea (El equivalente a mi docker-compose.yml)
resource "aws_ecs_task_definition" "n8n_task" { # Recurso tipo tarea de ECS
  family                   = "n8n-task"         # Nombre de la tarea
  requires_compatibilities = ["FARGATE"]        # Requisito de compatibilidad
  network_mode             = "awsvpc"           # Exigido por Fargate para aislar redes
  cpu                      = 256                # 0.25 vCPU (Potencia de procesamiento)
  memory                   = 512                # 512 MB de RAM

  # Aquí defino el contenedor usando formato JSON
  container_definitions = jsonencode([
    {
      name      = "n8n"              # Nombre del contenedor
      image     = "n8nio/n8n:latest" # Imagen de n8n
      essential = true               # El contenedor debe estar en ejecución para que el servicio funcione

      # Expongo el puerto de la interfaz web
      portMappings = [
        {
          containerPort = 5678 # Puerto del contenedor
          hostPort      = 5678 # Puerto del host
        }
      ]

      # VARIABLES DE ENTORNO
      environment = [
        { name = "DB_TYPE", value = "postgresdb" },                                #Tipo de base de datos
        { name = "DB_POSTGRESDB_HOST", value = aws_db_instance.postgres.address }, # Host de la base de datos se encuentra en el archivo rds.tf
        { name = "DB_POSTGRESDB_PORT", value = "5432" },                           # Puerto de la base de datos
        { name = "DB_POSTGRESDB_DATABASE", value = var.db_name },                  # Nombre de la base de datos se encuentra en el archivo variables.tf
        { name = "DB_POSTGRESDB_USER", value = var.db_user },                      # Usuario de la base de datos se encuentra en el archivo variables.tf
        { name = "DB_POSTGRESDB_PASSWORD", value = var.db_password },              # Contraseña de la base de datos se encuentra en el archivo variables.tf
        { name = "GENERIC_TIMEZONE", value = "Europe/Madrid" }                     # Zona horaria
      ]
    }
  ])
}


# Su trabajo es asegurar que tu contenedor esté siempre encendido.
resource "aws_ecs_service" "n8n_service" {               # Recurso tipo servicio de ECS
  name            = "n8n-service"                        # Nombre del servicio
  cluster         = aws_ecs_cluster.homelab_cluster.id   # Cluster al que pertenece el servicio
  task_definition = aws_ecs_task_definition.n8n_task.arn # Tarea que pertenece al servicio
  launch_type     = "FARGATE"                            # Tipo de lanzamiento

  # Aquí le decimos cuántas copias exactas de n8n queremos funcionando a la vez. 
  # Si pones 1 y el contenedor explota, el Service detectará que hay 0 y levantará otro nuevo para volver a tener 1.
  desired_count = 1

  # Como usamos Fargate (awsvpc), AWS nos obliga a conectarlo a una red física
  network_configuration {
    subnets          = []   # TODO: Aquí pondremos las subredes de tu VPC
    security_groups  = []   # TODO: Aquí pondremos el muro de fuego web
    assign_public_ip = true # Fundamental para que el contenedor tenga salida a internet y tú puedas entrar al panel
  }
}

