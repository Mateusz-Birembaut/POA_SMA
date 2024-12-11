class_name Menu extends Node2D

@onready var PlayButton: Button = %PlayButton
@onready var ExitButton: Button = %ExitButton

@onready var NbSlider: HSlider = %NbSlider
@onready var NbSliderLabel: Label = %NbSliderLabel
@onready var SpeedSlider: HSlider = %SpeedSlider
@onready var SpeedSliderLabel: Label = %SpeedSliderLabel
@onready var CandySlider: HSlider = %CandySlider
@onready var CandySliderLabel: Label = %CandySliderLabel
@onready var MenuBox: VBoxContainer = %MenuBox

@onready var menu_X = 2 * get_window().size.x / 3 - MenuBox.size.x / 2
@onready var menu_Y = get_window().size.y / 2 - MenuBox.size.y / 2


func _ready() -> void:
	PlayButton.position = Vector2i(
		get_window().size.x / 3 - 100,
		get_window().size.y / 2 - 50
	)

	ExitButton.position = Vector2i(
		get_window().size.x / 3 - 100,
		get_window().size.y / 2 + 50
	)

	###### MENU ######
	MenuBox.position = Vector2i(
		menu_X,
		menu_Y
	)
	
	NbSlider.value = GM.number_of_students
	CandySlider.value = GM.initial_cheese
	SpeedSlider.value = GM.prof_speed / 1000


func _on_play_button_pressed() -> void:
	GM.number_of_students = int(NbSlider.value)
	GM.initial_cheese = int(CandySlider.value)
	GM.prof_speed = int(SpeedSlider.value) * 1000
	get_tree().change_scene_to_file("res://src/main.tscn")


func _on_exit_button_pressed() -> void:
	get_tree().quit()


func _on_nb_slider_value_changed(value: float) -> void:
	NbSliderLabel.text = "Nombre d'étudiants : %s" % value


func _on_speed_slider_value_changed(value: float) -> void:
	SpeedSliderLabel.text = "Vitesse de la maîtresse : %s" % value


func _on_candy_slider_value_changed(value: float) -> void:
	CandySliderLabel.text = "Nombre de fromages : %s" % value
