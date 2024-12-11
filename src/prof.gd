extends Agent


var student_to_chase : Agent


func _ready() -> void:
	super._ready()
	speed = 7500
	position = Vector2i(95, 573)


func _process(delta: float) -> void:
	match state:
		States.WORK:
			check_students()

		States.CHASE:
			#check_students() # a commenter si on ne veut pas changer de "cible"
			nav.target_position = student_to_chase.position
			look_towards(nav.get_next_path_position())

			if (position - student_to_chase.position).length() <= 40:
				print(name, " renvoit un élève au travail")
				student_to_chase.send_to_work()
				print(name, " passe à l'état COMEBACK")
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
				print(name, " passe à l'état WORK")
				state = States.WORK
			check_students()


func _physics_process(delta):
	if env.DEBUG:
		var direction_x = Input.get_axis("ui_left", "ui_right")
		var direction_y = Input.get_axis("ui_up", "ui_down")

		if direction_x and direction_y:
			velocity.x = direction_x * speed * delta
			velocity.y = direction_y * speed * delta
			move_and_slide()
		else:
			super._physics_process(delta)
	else:
		super._physics_process(delta)


#func check_students() -> void:
	#student_to_chase = null
	#var shortest_distance := INF
	#var distance : float
	#for student in env.students:
		#distance = (student.position - env.candies.position).length()
		#if distance < 100 and distance < shortest_distance:
			#print("a student is not working !!!!!")
			#shortest_distance = distance
			#student_to_chase = student
			#print(name, " passe à l'état CHASE")
			#state = States.CHASE


func check_students() -> void:
	#if student_to_chase == null:
		student_to_chase = env.get_closest_student_to_candies()
		if student_to_chase != null:
			print("a student is not working !!!!!")
			print(name, " passe à l'état CHASE")
			state = States.CHASE


func see() -> void:
	# get la position de l'eleve le plus proche des bonbons qui soit parti 

	#if studentPosition != null :
		# state = CHASE
	#else:
		#if position == initial_position :
			#state = WORK
		#else :
			#state = COMEBACK 

	pass


func action() -> void:
	pass
