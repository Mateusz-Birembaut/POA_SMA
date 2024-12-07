class_name Env extends Node2D


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
