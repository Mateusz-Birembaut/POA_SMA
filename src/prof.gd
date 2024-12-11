extends Agent


var student_to_chase : Agent


func _ready() -> void:
	super._ready()
	speed = GM.prof_speed


func _process(delta: float) -> void:
	match state:
		States.WORK:
			check_students()

		States.CHASE:
			if student_to_chase.state == States.COMEBACK:
				check_students() 
			
			if student_to_chase == null:
				state = States.COMEBACK
				look_towards(initial_position)
			else :
				nav.target_position = student_to_chase.position
				look_towards(nav.get_next_path_position())
				if (position - student_to_chase.position).length() <= 40:
					env.debug_print(name, " renvoit un élève au travail")
					student_to_chase.send_to_work()
					env.debug_print(name, " passe à l'état COMEBACK")
					state = States.COMEBACK

		States.COMEBACK:
			if (nav.get_final_position() - global_position).length() > 30:
				nav.target_position = initial_position
				look_towards(nav.get_next_path_position())
			else:
				look_towards(initial_position)
			if (position - initial_position).length() <= 5:
				nav.target_position = Vector2()
				velocity = Vector2()
				env.debug_print(name, " passe à l'état WORK")
				state = States.WORK
			check_students()


func check_students() -> void:
		student_to_chase = env.get_closest_student_to_candies()
		if student_to_chase != null:
			env.debug_print(name, " a student is not working !!!!!")
			env.debug_print(name, " passe à l'état CHASE")
			state = States.CHASE
