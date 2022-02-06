from apscheduler.schedulers.background  import BlockingScheduler
from Html_script import retrieve_html
sched = BlockingScheduler()


def maina():
    """Run tick() at the interval of every ten seconds."""
   
    sched.add_job(retrieve_html, 'interval', minutes=6)
    try:
        sched.start()
    except (KeyboardInterrupt, SystemExit):
        pass 


maina()


