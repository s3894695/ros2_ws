from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    ld = LaunchDescription()

    # Use find_package to locate the paths of the individual packages
    rosbot_controller_pkg_dir = get_package_share_directory('rosbot_controller')
    #rosbot_description_pkg_dir = get_package_share_directory('rosbot_description')
    nav2_bringup_pkg_dir = get_package_share_directory('nav2_bringup')
    rosbot_bringup_pkg_dir = get_package_share_directory('rosbot_bringup')

    # Add the launch files of the individual packages
    rosbot_controller_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(rosbot_controller_pkg_dir + '/launch/controller.launch.py')
    )
    '''rosbot_description_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(rosbot_description_pkg_dir + '/launch/rosbot_pro.launch.py')
    )'''

    rosbot_bringup_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(rosbot_bringup_pkg_dir + '/launch/bringup.launch.py')
    )

    nav2_bringup_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(nav2_bringup_pkg_dir + '/launch/navigation_launch.py')
    )

    nav2_bringup_loc_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(nav2_bringup_pkg_dir + '/launch/localization_launch.py')
    )

    # Add the actions to the launch description
    ld.add_action(rosbot_controller_launch)
    #ld.add_action(rosbot_description_launch)
    ld.add_action(rosbot_bringup_launch)
    ld.add_action(nav2_bringup_launch)
    ld.add_action(nav2_bringup_loc_launch)

    return ld
