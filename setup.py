from distutils.core import setup

setup(
    name='SFL-diagnoser',
    version='0.0.1',
    packages=['Planner', 'Planner.mcts', 'Planner.lrtdp', 'Planner.pomcp', 'Planner.pomcp_old.pomcp',
              'Planner.lrtdp_checker', 'Diagnoser'],
    url='https://github.com/amir9979/SFL-diagnoser',
    license='',
    author='Amir Elmishali',
    author_email='amir9979@gmail.com',
    description='spectrum-based fault localization diagnoser'
)
