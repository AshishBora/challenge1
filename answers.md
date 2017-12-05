- How did you verify that you are parsing the contours correctly?

    Created the file `test_countour.txt` with four corners. Verified that the values are properly read.
    Also verfied that the central square indicated by the `test_countour.txt` file indeed becomes all true.

- What changes did you make to the code, if any, in order to integrate it into our production code base?

    Added tests in `parsing_test.py` for functions in `parsing.py`

- Did you change anything from the pipelines built in Parts 1 to better streamline the pipeline built in Part 2? If so, what? If not, is there anything that you can imagine changing in the future?

    Not really. I had already created the Datapoint class, so it was easy to make a pipeline by passing a list of Datapoints to the DataFeeder.

- How do you/did you verify that the pipeline was working correctly?

    See tests in `feeding_test.py`

- Given the pipeline you have built, can you see any deficiencies that you would change if you had more time? If not, can you think of any improvements/enhancements to the pipeline that you could build in?

    The current pipeline loads all the data in memory. For large datasets this is not really a good strategy. In that case, the Datapoint class can instead hold only the path to the dicom and contour images and the actual data can be read on demand inside the next_batch or package function.
