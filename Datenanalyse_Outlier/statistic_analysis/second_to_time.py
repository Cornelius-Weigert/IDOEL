import math

def second_to_time(seconds: float) -> str:
    """
    Konvertiert eine Zeitangabe in Sekunden in ein lesbares Zeitformat.

    Parameter:
        seconds (float): Zeit in Sekunden.

    Rückgabewert:
        str: Lesbare Zeitangabe 
    """
    
    if seconds is None or (isinstance(seconds, float)and math.isnan(seconds)):
        return "-"
    else:
        seconds = int(abs(seconds))
        seconds = int(abs(seconds))

        years, seconds = divmod(seconds, 365 * 24 * 3600)
        months, seconds = divmod(seconds, 30 * 24 * 3600)
        days, seconds = divmod(seconds, 24 * 3600)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)

        time= []
        if years: time.append(f"{years}y ")
        if months: time.append(f"{months}mo ")
        if days: time.append(f"{days}d ")
        if hours: time.append(f"{hours}h ")
        if minutes: time.append(f"{minutes}min ")
        if seconds or not time: time.append(f"{seconds}s ")

        return "".join(time)

   