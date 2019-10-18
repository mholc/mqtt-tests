## Dependencies

```
pip install paho-mqtt
```

## Test steps

1. Setup conf.py, and possibly fix the SSL context if needed. 
2. Run `python test.py`. This will subscribe to topics named `test/topic/{id}/+` where `id` is a number between 0 and 100. The script will print out the time subscription took, usually around less than 0.02 s in our environment. Press `ctrl-c` to exit. 
3. Run `python dump.py < testtopics`. This will populate topics listed in `testtopics` file with a small amount of retained data.
4. Run `python test.py` again. This time, subscription to unrelated topics is considerably slower, and usually takes almost 3 seconds.
5. Run `python clean.py < testtopics`. This will publish `None` to each topic listed in `testtopics` to clean up the retained messages.
6. Run `python test.py` again. This time, subscription to unrelated topics is again fast.


 