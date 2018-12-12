class State(object):
    def __init__(self, name):
        self._name = name

    def run(self):
        # doing nothing, this will be overriden later.
        pass

    def next(self, input):
        # do nothing, stay in the same state.
        return self

    def __str__(self):
        return self._name

class StateMachine(object):
    def __init__(self, initial_state):
        self._current_state = initial_state

        self._next_state = None

    # this will serve us now to check the state machine, that we wrote . will be changed tommorow .
    def _demo_states(self, inputs):
        print( 'starting state machines, inputs: {}'.format(inputs))
        for input in inputs:
            self.run_state(input)
        print('done with demo.')

    def run_state(self, input):
        print(' running state: {}'.format(self._current_state))
        self._current_state.run()
        self._next_state = self._current_state.next(input)
        self._current_state = self._next_state




def main():
    s = State('test_state')
    print(s)
if __name__ == "__main__":
    main()