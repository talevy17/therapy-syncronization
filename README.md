
## Project Overview

In this project we have split the work to two main parts

### `Algorithms`

`Implementaion of LSM`<br />
The implementation, given a transcription of a conversation between two people, calculates the LSM between two people.

`Coordination Evalutaion`<br />
Calculates the level of influence one speaker have on the other.

`Output Format`<br />
The output we provide is csv tabels of the results and graphs presenting them.

`Usage`<br />
See the algorithm directory for more info. <br />
https://github.com/talevy17/therapy-syncronization/tree/master/algorithms

### `Demo`

The demo presents our work<br />
It previews some information about the lab in general, what we have implemented, the results on our data, and the possibilty of uploading data to the server and getting their LSM\Coordination values proccessed.
see https://github.com/talevy17/therapy-syncronization/tree/master/demo for more info.

`Api`
Using Flask to open endpoints.<br />
Provides the bridge between the client side of the demo to the algorithms.

## Running locally

### Client-Server App

See `Quick Start` in https://github.com/talevy17/therapy-syncronization/tree/master/demo for all the relevant information.

### Algorithms

You can also run the algorithms themselves outside of the Client-Server App, see https://github.com/talevy17/therapy-syncronization/tree/master/algorithms.