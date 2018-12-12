

import StateMachineReceipe

# input names
INPUT_EATING = 'eating'
INPUT_SHITTING = 'shit'
INPUT_NEED_SHIT = 'need_shit'
INPUT_DONE_SHITTING = 'done_shitting'

# state names
STATE_NOT_NEED_TO_SHIT = 'not_need_to_shit'
STATE_EATING = 'eating'
STATE_NEED_TO_SHIT = 'need_shit'
STATE_SHITTING = 'shitting'


class StateNotNeedToShit(StateMachineReceipe.State):
    def __init__(self):
        super(StateNotNeedToShit, self).__init__(STATE_NOT_NEED_TO_SHIT)

    def run(self):
        print('hello , i dont need to shit')

    def next(self, input):
        if (input == INPUT_EATING):
            return states[STATE_EATING]
        return self

class StateEating(StateMachineReceipe.State):
    def __init__(self):
        super(StateEating, self).__init__(STATE_EATING)

    def run(self):
        print('I am eating ....')

    def next(self, input):
        if( input == INPUT_EATING):
            return states[STATE_EATING]
        elif (input == INPUT_NEED_SHIT):
            return states[STATE_NEED_TO_SHIT]
        else:
            return self

class StateNeedToShit(StateMachineReceipe.State):
    def __init__(self):
        super(StateNeedToShit, self).__init__(STATE_NEED_TO_SHIT)

    def run(self):
        print('I need to shit ....')

    def next(self, input):
        if (input == INPUT_SHITTING):
            return states[STATE_SHITTING]
        return self

class StateShitting(StateMachineReceipe.State):
    def __init__(self):
        super(StateShitting, self).__init__(STATE_SHITTING)

    def run(self):
        print('I am shitting ....')

    def next(self, input):
        if (input == INPUT_SHITTING):
            return self
        elif (input == INPUT_DONE_SHITTING):
            return states[STATE_NOT_NEED_TO_SHIT]
        return self



class TakingShitSM(StateMachineReceipe.StateMachine):
    def __init__(self, init_state):
        # call base ctor.
        super(TakingShitSM, self).__init__(init_state)

    def run_states(self, inputs):
        for input in inputs:
            self.run_state(input)

states = {STATE_NOT_NEED_TO_SHIT : StateNotNeedToShit(),
          STATE_EATING : StateEating(),
          STATE_NEED_TO_SHIT: StateNeedToShit(),
          STATE_SHITTING: StateShitting()}

def main():
    init_state = states[STATE_NOT_NEED_TO_SHIT]
    sm = TakingShitSM(init_state)

    # at the moment , predefine all the inputs, later we try something else.
    inputs = [INPUT_EATING, INPUT_EATING, INPUT_NEED_SHIT, INPUT_SHITTING, INPUT_DONE_SHITTING, INPUT_EATING]
    sm.run_states(inputs)
    print('Done - am at state: {}'.format(sm._current_state))

if __name__ == "__main__":
    main()