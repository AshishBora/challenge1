- After building the pipeline, please discuss any changes that you made to the pipeline you built in Phase 1, and why you made those changes.

    All changes to the pipeline can be seen in the following commit:
    https://github.com/AshishBora/challenge1/commit/c8e1dacfc5542f0668091862f40d13d79796aa14

    In summary:
    1. Changed Datapoint class to also hold ocountours
    2. Changed `intersection` function to be more generic
    3. Added reading and mask creation for o-contour files

- Let’s assume that you want to create a system to outline the boundary of the blood pool (i-contours), and you already know the outer border of the heart muscle (o-contours). Compare the differences in pixel intensities inside the blood pool (inside the i-contour) to those inside the heart muscle (between the i-contours and o-contours); could you use a simple thresholding scheme to automatically create the i-contours, given the o-contours? Why or why not? Show figures that help justify your answer. Do you think that any other heuristic (non-machine learning)-based approaches, besides simple thresholding, would work in this case? Explain.

    Please see the ipython notebook `analysis.ipynb` for a detailed discussion.
