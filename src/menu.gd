class_name Menu extends Node2D


@onready var play_button: Button = $PlayButton
@onready var quit_button: Button = $QuitButton
@onready var vbox: VBoxContainer = $VBoxContainer
@onready var student_label: Label = %StudentLabel
@onready var student_slider: HSlider = %StudentSlider
@onready var speed_label: Label = %SpeedLabel
@onready var speed_slider: HSlider = %SpeedSlider
@onready var cheese_label: Label = %CheeseLabel
@onready var cheese_slider: HSlider = %CheeseSlider


func _ready() -> void:
	play_button.position = Vector2i(get_viewport_rect().size.x / 3 - 100, get_viewport_rect().size.y / 2 - 50)

	quit_button.position = Vector2i(get_viewport_rect().size.x / 3 - 100, get_viewport_rect().size.y / 2 + 50)

	vbox.position = Vector2i(2 * get_viewport_rect().size.x / 3 - vbox.size.x / 2,
							get_viewport_rect().size.y / 2 - vbox.size.y / 2)

	student_slider.value = GM.number_of_students
	cheese_slider.value = GM.initial_cheese
	speed_slider.value = GM.prof_speed / 1000


func _on_play_button_pressed() -> void:
	GM.number_of_students = int(student_slider.value)
	GM.initial_cheese = int(cheese_slider.value)
	GM.prof_speed = int(speed_slider.value) * 1000
	get_tree().change_scene_to_file("res://src/main.tscn")


func _on_exit_button_pressed() -> void:
	get_tree().quit()


func _on_student_slider_value_changed(value: float) -> void:
	student_label.text = "Nombre d'étudiants : %s" % value


func _on_speed_slider_value_changed(value: float) -> void:
	speed_label.text = "Vitesse de la maîtresse : %s" % value


func _on_cheese_slider_value_changed(value: float) -> void:
	cheese_label.text = "Nombre de fromages : %s" % value
