@tool
extends Agent


const SPEED = 300.0
const JUMP_VELOCITY = -400.0


#func _ready() -> void:
	#pass


#func _process(delta: float) -> void:
	# if CHASE => se déplacer vers l'eleve plus proche bonbons
		#move_towards()
	# if COMEBACK => se déplacer vers la table
		# direction = tablePosition - position . normalize
		# position = position + direction * speed
	# if WORK => ne rien faire
	
	#pass


func _physics_process(delta):
	# Add the gravity.
	#if not is_on_floor():
		#velocity += get_gravity() * delta

	# Handle jump.
	if Input.is_action_just_pressed("ui_accept") and is_on_floor():
		velocity.y = JUMP_VELOCITY

	# Get the input direction and handle the movement/deceleration.
	# As good practice, you should replace UI actions with custom gameplay actions.
	var direction_x = Input.get_axis("ui_left", "ui_right")
	var direction_y = Input.get_axis("ui_up", "ui_down")
	#if direction_x:
	velocity.x = direction_x * SPEED
	velocity.y = direction_y * SPEED
	#else:
	#velocity.x = move_toward(velocity.x, 0, SPEED)
	move_and_slide()


func see() -> void:
	# get la position de l'eleve le plus proche  des bonbon qui soit parti 
	
	#if studentPosition != null :
		# state = CHASE
	#else:
		#if position == initial_position :
			#state = WORK
		#else :
			#state = COMEBACK 

	pass
