from setuptools import setup

setup(
    name='SFL-diagnoser',
    version='0.0.1',
    packages=['SFL_diagnoser', 'SFL_diagnoser.Planner', 'SFL_diagnoser.Planner.mcts', 'SFL_diagnoser.Planner.lrtdp',
              'SFL_diagnoser.Planner.pomcp', 'SFL_diagnoser.Planner.pomcp_old', 'SFL_diagnoser.Planner.pomcp_old.pomcp',
              'SFL_diagnoser.Planner.lrtdp_checker', 'SFL_diagnoser.Diagnoser'],
    url='https://github.com/amir9979/SFL-diagnoser',
    license='',
    author='Amir Elmishali',
    author_email='amir9979@gmail.com',
    description='spectrum-based fault localization diagnoser'
)
