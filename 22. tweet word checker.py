def twt_chk(tweet:str) -> bool:
    for chr in tweet:
        if not ( chr.isalnum() or chr == '_' ):
            return False
    return True

