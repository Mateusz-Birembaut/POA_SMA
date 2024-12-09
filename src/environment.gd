class_name Env extends Node2D


const DEBUG := true

@export_range(1, 20)
var number_of_students := 5

@onready var desk = %Desk
@onready var candies = %Candies
@onready var prof : Agent = %Prof

var student_scene := preload("res://src/student.tscn")
var students : Array[Agent]


func _ready() -> void:
	var x := get_window().size.x/2 - (number_of_students * 50)/2 + 25
	for i in number_of_students:
		var new_student : Agent = student_scene.instantiate()
		new_student.position = Vector2i(x, desk.position.y-40-25)
		add_child(new_student)
		students.append(new_student)
		x += 50
		
func get_closest_student_to_candies() -> Agent:
	var student_to_chase = null
	var min_distance = 100000
	for student in students:
		if student.state == Agent.States.LEAVE:
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
				
