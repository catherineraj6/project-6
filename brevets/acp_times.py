"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_acp.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#
open_list = [(200,200,34),(400,200,32),(600,200,30),(1000,400,28),(1300,300,26)]
close_list = [(600,600,15),(1000,600,11.428),(1300,1000,13.333)]




def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    minutes = 0
    if brevet_dist_km < control_dist_km:
        control_dist_km = brevet_dist_km
    for i in open_list:
        num1, num2, num3 = i
        if control_dist_km > num1:
            minutes += (num2 / num3) * 60
        else:
            minutes += ((control_dist_km-(num1-num2))/num3) * 60
            break
    round_var = round(minutes)
    return brevet_start_time.shift(minutes=round_var)


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    minutes = 0

    if brevet_dist_km < control_dist_km:
        control_dist_km = brevet_dist_km
    for i in close_list:
        num1, num2, num3 = i
        
        if control_dist_km > num1:
            round1 = round((num2 /num3) * 60)
            minutes += round1
        else:
            if control_dist_km <= 60: 
                round2 = round((control_dist_km/20 + 1) *60)
                minutes += round2
                break
            elif control_dist_km <= 600:
                round3 = round((control_dist_km/15) * 60)
                minutes += round3
                break
        
            round4 = round(((control_dist_km - num2) / num3) * 60)
            minutes += round4
        
    round_var = round(minutes)
    return brevet_start_time.shift(minutes=round_var)