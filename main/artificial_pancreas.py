class ArtificialPancreasSystem:
    """A simplified model for data-driven glucose regulation."""
        
    GLUCOSE_PER_CARB = 0.5      # fixed increase per carb unit
    GLUCOSE_BURN_PER_MIN = 0.3  # fixed decrease per minute of exercise


    def __init__(self, glucose_level, insulin_sensitivity=1.0, target_glucose=100, tolerance=10):
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

    def deliver_insulin(self, units: float):
        """Simulate insulin delivery (input feature: units)."""
        if self.glucose_level <= 50:
            pass
        else:
            self.glucose_level -= units * self.insulin_sensitivity

    def warn_low_glucose(self):        
        return "Warning: Critically low glucose level!"
    
    def carb_intake_needed(self):
        return (self.target_glucose - self.glucose_level) / self.GLUCOSE_PER_CARB
    
    def suggest_carb_intake(self):
        return f"Suggestion: Consume {carb_intake_needed()}carbs to raise glucose level."
            
    def maintain_glucose(self):
        return "Maintian: Glucose level is stable."

    def predict_action(self):
        """
        Predict and apply an appropriate system action.
        Acts like a decision function in a model.
        """
        if self.glucose_level > self.target_glucose + self.tolerance:
            # High glucose - deliver insulin
            insulin_dose = (self.glucose_level - self.target_glucose) / self.insulin_sensitivity
            self.deliver_insulin(insulin_dose)
            return ("Delivered Insulin", f"New glucose level:{self.glucose_level}")
        
        elif self.glucose_level < self.target_glucose - self.tolerance:
            carb_intake_needed = self.carb_intake_needed()
            # Low glucose - warn and suggest carbohydrate intake
            self.meal(carb_intake_needed)
            return (f"{self.warn_low_glucose()}.\n{self.suggest_carb_intake()}", f"New glucose level:{self.glucose_level}")
        else:
            # Stable glucose
            return(self.maintain_glucose(), f"Current glucose level:{self.glucose_level}")
        