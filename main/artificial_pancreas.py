class ArtificialPancreasSystem:
    """A simplified model for data-driven glucose regulation."""
        
    GLUCOSE_PER_CARB = 0.5      # fixed increase per carb unit
    GLUCOSE_BURN_PER_MIN = 0.3  # fixed decrease per minute of exercise

    def __init__(self, glucose_level, insulin_sensitivity=1.0, target_glucose=100.0, tolerance=10.0):
        self.glucose_level = glucose_level
        self.insulin_sensitivity = insulin_sensitivity
        self.target_glucose = target_glucose
        self.tolerance = tolerance

    def meal(self, carbs: float):
        """Simulate a meal event (input feature: carbs)."""
        self.glucose_level += carbs * self.GLUCOSE_PER_CARB
        
    def exercise(self, duration: float):
        """Simulate physical activity (input feature: duration)."""
        self.glucose_level -= duration * self.GLUCOSE_BURN_PER_MIN

    def insulin_dose_needed(self):
        print("Calculating insulin dose needed...")
        self.insulin_dose_needed = (self.glucose_level - self.target_glucose) / self.insulin_sensitivity
        print(f"You need {self.insulin_dose_needed} units of insulin.")
        return self.insulin_dose_needed

    def deliver_insulin(self, units: float):
        """Simulate insulin delivery (input feature: units)."""
        if self.glucose_level <= 50:
            pass
        else:
            print(f"Delivering {units} units of insulin...")
            self.glucose_level -= units * self.insulin_sensitivity
    
    def carb_intake_needed(self):
        return 2 * (self.target_glucose - self.glucose_level)

    def warn_low_glucose(self):
        return f"Warning: Critically low glucose level!. You need {self.carb_intake_needed()} carbs immediately."
    
    def maintain_glucose(self):
        return "Maintian: Glucose level is stable."

    def predict_action(self):
        """
        Predict and apply an appropriate system action.
        Acts like a decision function in a model.
        """
        if self.glucose_level > self.target_glucose + self.tolerance:
            # High glucose - deliver insulin
            insulin_dose_needed = self.insulin_dose_needed()
            self.deliver_insulin(insulin_dose_needed)
            return (f"{self.deliver_insulin.__name__}:", f"New glucose level:{self.glucose_level}")
        
        elif self.glucose_level < (self.target_glucose - self.tolerance):
            # Low glucose - warn and suggest carbohydrate intake
            print(f"{self.warn_low_glucose()}")
            self.meal(self.carb_intake_needed())
            return (f"{self.warn_low_glucose.__name__}:", f"New glucose level: {self.glucose_level}")
        
        else:
            # Stable glucose
            return (f"{self.maintain_glucose.__name__}:", f"Current glucose level: {self.glucose_level}")
        git