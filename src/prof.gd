extends Agent


var student_to_chase : Agent


func _ready() -> void:
	super._ready()
	speed = 7500


func _process(delta: float) -> void:
	# if CHASE => se déplacer vers l'eleve plus proche bonbons
		#move_towards()
	# if COMEBACK => se déplacer vers la table
		# direction = tablePosition - position . normalize
		# position = position + direction * speed
	# if WORK => regarder si des élèves s'approche des bonbons

	match state:
		States.WORK:
			check_students()
		States.CHASE:
			look_towards(student_to_chase.position)
			if (position - student_to_chase.position).length() <= 50:
				print(name, " renvoit un élève au travail")
				student_to_chase.send_to_work()
				print(name, " passe à l'état COMEBACK")
				state = States.COMEBACK
		States.COMEBACK:
			look_towards(initial_position)
			if (position - initial_position).length() <= 1:
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
	if student_to_chase == null:
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
