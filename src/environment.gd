class_name Env extends Node2D


const DEBUG := true

@export_range(1, 3)
var number_of_rows := 1

@onready var candies = %Candies
@onready var prof : Agent = %Prof
@onready var score = get_node("Score")
@onready var timer = get_node("Timer")

var student_scene := preload("res://src/student.tscn")
var students : Array[Agent]
var desk_scene := preload("res://src/desk.tscn")

var total_candies = 10
var time_elapsed = 0

func update_score() -> void:
	total_candies -= 1
	if total_candies == 0:
		get_tree().paused = true
	print(total_candies)
	score.text = str(total_candies)


func _process(delta: float) -> void:
	time_elapsed += delta
	timer.text = str(snapped(time_elapsed, 0.01))

func _ready() -> void:
	timer.position.x = get_window().size.x/2 - 25
	score.text = str(total_candies)
	var y := 150
	for i in number_of_rows:
		var x := 200
		for j in 5:
			var new_desk : Sprite2D = desk_scene.instantiate()
			new_desk.position = Vector2i(x, y)
			add_child(new_desk)
			var new_student : Agent = student_scene.instantiate()
			new_student.position = Vector2i(x, y)
			add_child(new_student)
			students.append(new_student)
			x += 120 + 65
		y += 80 + 40


func get_closest_student_to_candies() -> Agent:
	var student_to_chase = null
	var min_distance = 100000
	for student in students:
		if student.state == Agent.States.LEAVE or student.state == Agent.States.COLLECT  :
			var distanceToCandies = (student.position - candies.position).length()
			if distanceToCandies < min_distance:
				min_distance = distanceToCandies
				student_to_chase = student
	return student_to_chase


func get_number_ready_student() -> int:
	var nb_ready = 0
	for student in students:
		if student.state == Agent.States.READY:
			nb_ready += 1

	return nb_ready


func signal_go() -> void :
	for student in students:
		if student.state == Agent.States.READY:
			student.state = Agent.States.LEAVE
