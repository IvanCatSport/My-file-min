# coding: utf8

import rospy
from clover import srv
from std_srvs.srv import Trigger

  rospy.init_node('flight')

   
    navigate = rospy.ServiceProxy('navigate', srv.Navigate)
 
     navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)

        set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)

         set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)

             land = rospy.ServiceProxy('land', Trigger)

              # Взлет на высоту 1 м
                  navigate(x=0, y=0, z=1, frame_id='body', auto_arm=True)

                    # Ожидание 3 секунды
                      rospy.sleep(3)

                         # Пролет вперед 1 метр
                           navigate(x=1, y=0, z=0, frame_id='body')

                             # Ожидание 3 секунды
                                rospy.sleep(3)
                                 # Пасадка
                                      land()