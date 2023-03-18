import nose
import logging
import arrow
from mymongo import insert_brevet, get_brevet

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

def test_insert_brev():
    start_time = arrow.get("2023-02-23 00:00", "YYYY-MM-DD HH:mm")
    brevet_dist = 200
    checkpoints = {
        0:  (start_time, start_time.shift(hours=1)),
        50: (start_time.shift(hours=1, minutes=28),start_time.shift(hours=3.5)),
        150:(start_time.shift(hours=4, minutes=25),start_time.shift(hours=10)),
        200:(start_time.shift(hours=5, minutes=53),start_time.shift(hours=13.5))
    
    }
    check = insert_brevet(start_time,brevet_dist,checkpoints)
    assert isinstance(check, str)

def test_fetch_brev():
    start_time = arrow.get("2023-02-23 00:00", "YYYY-MM-DD HH:mm")
    brevet_dist = 200
    checkpoints = {
        0:  (start_time, start_time.shift(hours=1)),
        50: (start_time.shift(hours=1, minutes=28),start_time.shift(hours=3.5)),
        150:(start_time.shift(hours=4, minutes=25),start_time.shift(hours=10)),
        200:(start_time.shift(hours=5, minutes=53),start_time.shift(hours=13.5))
    
    }
    check1 = insert_brevet(start_time,brevet_dist,checkpoints)
    check2 = get_brevet()
    assert isinstance(check2,str)



