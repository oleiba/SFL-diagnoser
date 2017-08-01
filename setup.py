from setuptools import setup

setup(
    name='SFL-diagnoser',
    version='0.0.1',
    packages=['sfl_diagnoser', 'sfl_diagnoser.Planner', 'sfl_diagnoser.Planner.mcts', 'sfl_diagnoser.Planner.lrtdp',
              'sfl_diagnoser.Planner.pomcp', 'sfl_diagnoser.Planner.pomcp_old', 'sfl_diagnoser.Planner.pomcp_old.pomcp',
              'sfl_diagnoser.Planner.lrtdp_checker', 'sfl_diagnoser.Diagnoser'],
    url='https://github.com/amir9979/SFL-diagnoser',
    license='',
    author='Amir Elmishali',
    author_email='amir9979@gmail.com',
    description='spectrum-based fault localization diagnoser'
)
