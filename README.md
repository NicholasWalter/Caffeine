Very tiny python project that forces screen to remain turned on by sending control key inputs at specified intervals.

## usage:
### bash:
```
chmod +x caffeine.sh
./caffeine.sh [interval]
```

### python:
```
python3.x caffeine.py [interval]
```

If no interval is specified, will send a key every 60 seconds, default interval can be changed in source code.

## global use
copy caffeine.sh file and caffeine_implementation folder to /bin/

//I know there are more elegant solutions but I needed this quickly and it works.