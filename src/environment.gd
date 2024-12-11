class_name Env extends Node2D


const DEBUG := true

@export_range(1, 15)
var number_of_students := 4

@onready var cheeses = %Cheeses
@onready var prof : Agent = %Prof
@onready var score : Label = $Score
@onready var timer : Label = $Timer

var cheese0 := preload("res://assets/plate0.png")
var cheese1 := preload("res://assets/plate1.png")
var cheese2 := preload("res://assets/plate2.png")
var cheese3 := preload("res://assets/plate3.png")
var cheese4 := preload("res://assets/plate4.png")
var cheese5 := preload("res://assets/plate5.png")
var cheese6 := preload("res://assets/plate6.png")
var student_scene := preload("res://src/student.tscn")
var students : Array[Agent]
var desk_scene := preload("res://src/desk.tscn")

var initial_cheese := 10
var remaining_cheese := initial_cheese
var time_elapsed := 0


func update_score() -> void:
	remaining_cheese -= 1
	var remaining_cheese_ratio : float = remaining_cheese * 1.0 / initial_cheese
	var new_texture
	if remaining_cheese_ratio == 0:
		new_texture = cheese0
	elif remaining_cheese_ratio < 0.167:
		new_texture = cheese1
	elif remaining_cheese_ratio < 0.333:
		new_texture = cheese2
	elif remaining_cheese_ratio < 0.50:
		new_texture = cheese3
	elif remaining_cheese_ratio < 0.667:
		new_texture = cheese4
	elif remaining_cheese_ratio < 0.833:
		new_texture = cheese5
	else:
		new_texture = cheese6
	cheeses.get_node("Sprite2D").texture = new_texture
	if remaining_cheese == 0:
		get_tree().paused = true
	print(remaining_cheese)
	score.text = str(remaining_cheese)


func _process(delta: float) -> void:
	time_elapsed += delta
	timer.text = str(snapped(time_elapsed, 0.01))


func _ready() -> void:
	timer.position.x = get_window().size.x/2 - 25
	score.text = str(remaining_cheese)
	var nb_student_lure = 0
	var y := 100
	for i in 3:
		var x := 200
		for j in 5:
			var new_desk : Sprite2D = desk_scene.instantiate()
			new_desk.position = Vector2i(x, y)
			add_child(new_desk)
			if i * 5 + j < number_of_students:
				var new_student : Agent = student_scene.instantiate()
				new_student.initial_position = Vector2i(x, y)
				new_student.scale = Vector2(0.6, 0.6)
				add_child(new_student)
				#new_student.agent.position = Vector2i(x, y)
				#new_student.mini_agent.position = Vector2i(x, y)
				if new_student.strategy == Student.Strategies.LURE:
					nb_student_lure += 1
				students.append(new_student)
			x += 120 + 65
		
		y += 80 + 40
	if nb_student_lure == 1:
		add_lure_student()


func get_closest_student_to_candies() -> Agent:
	var student_to_chase = null
	var min_distance = 100000
	for student in students:
		if student.state == Agent.States.LEAVE or student.state == Agent.States.COLLECT:
			var distanceToCandies = (student.position - cheeses.position).length()
			if distanceToCandies < min_distance:
				min_distance = distanceToCandies
				student_to_chase = student
	return student_to_chase


func get_number_ready_student() -> int:
	var nb_ready = 0
	for student in students:
		if student.state == Agent.States.READY and student.strategy != Student.Strategies.LURE:
			nb_ready += 1

	return nb_ready


func signal_friends_go(strategy :Student.Strategies) -> void :
	for student in students:
		if student.state == Agent.States.READY and student.strategy == strategy:
			student.state = Agent.States.LEAVE


func get_lure_ready_student() -> int :
	var nb_ready = 0
	for student in students:
		if student.state == Agent.States.READY and student.strategy == Student.Strategies.LURE:
			nb_ready += 1
	return nb_ready


func lure_exists() -> bool:
	for student in students:
		if student.strategy == Student.Strategies.LURE and student.lure:
				return true
	return false


func add_lure_student() -> void :
	while true:
		var rand_index = randi_range(0, number_of_students-1)
		if students[rand_index].strategy != Student.Strategies.LURE :
			students[rand_index].strategy = Student.Strategies.LURE
			students[rand_index].sprite.modulate = Color(1, 0, 0)
			return


func debug_print(name: StringName, text: String) -> void:
	if DEBUG:
		print(name, text)
