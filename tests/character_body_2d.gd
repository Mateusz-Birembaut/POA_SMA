extends CharacterBody2D


const SPEED = 200.0
const ACCEL = 4.0

@onready var nav : NavigationAgent2D = $NavigationAgent2D


func _physics_process(delta):
	var target_pos := get_global_mouse_position()
	if (target_pos - global_position).length() > 25:
		var direction := Vector2()

		nav.target_position = target_pos

		direction = (nav.get_next_path_position() - global_position).normalized()

		velocity = velocity.slerp(direction * SPEED, ACCEL * delta)

		move_and_slide()
