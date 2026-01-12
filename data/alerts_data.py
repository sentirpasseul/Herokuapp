from enum import StrEnum


class TestAlertsData(StrEnum):
    ALERT_TEXT = "I am a JS Alert"
    ALERT_RESULT_TEXT = "You successfully clicked an alert"

    CONFIRM_TEXT = "I am a JS Confirm"
    CONFIRM_RESULT_TEXT = "You clicked: Ok"

    PROMPT_TEXT = "I am a JS prompt"
    PROMPT_RESULT_TEXT = "You entered: "
