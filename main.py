from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.icon = "nerdy ahh.jpg"
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None

        main_layout = BoxLayout(orientation = "vertical") # using BoxLayout import
        # start of the screen
        self.solution = TextInput(background_color = "black", foreground_color = "white") # using Textinput import
        
        main_layout.add_widget(self.solution)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "C", "-"],
        ]

        # inser the buttons in the screen
        for row in buttons:
            h_layout = BoxLayout()
            for label in row: # creating the labels
                button = Button(
                    text = label, font_size = 30, background_color = "grey",
                    pos_hint = {"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press = self.on_button_press) # when the user presses this button, this function will activate
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout) # inserting the h_layout in the main layout
        # finished creating buttons

        equal_button = Button(
            text = "=", font_size = 30, background_color = "grey",
            pos_hint = {"center_x" : 0.5, "center_y": 0.5},
        )

        equal_button.bind(on_press = self.on_solution)
        main_layout.add_widget(equal_button)

        return main_layout
    
    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == 'C':
            self.solution.text = ""
        else:
            if current and ( # if 2 operators are typed
                self.last_was_operator and button_text in self.operators):
                return
            elif current == "" and button_text in self.operators: # if operator is typed 1st
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text

        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators
    
    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution

if __name__ == "__main__":
    app = MainApp()
    app.run()