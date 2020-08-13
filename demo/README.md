To run the demo locally make sure you have Python3 and npm or yarn installed.<br />
Also, make sure to `npm i` before your first run.

## Available Scripts

In the demo directory, you can run:

### `npm run start`

Runs the app in the development mode.<br />
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.<br />
You will also see any lint errors in the console.

### `npm run start-server`

Runs the server in development mode.<br />
Open [http://localhost:5000](http://localhost:5000) to view it in the browser.

Note that the upload data section of the demo requiers the server to run.<br />

### `npm run clean`

Cleans all node modules and build.<br />

### `npm run reinstall`

Cleans all node modules and build and then installs node modules.<br />

### `npm run build`

Builds the app for production to the `build` folder.<br />
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.<br />
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run rebuild`

Cleans all node modules and build and then installs node modules and builds.<br />

## Technical Info

The demo was build using `React/js` for the client side and `Python Flask` for the server side. <br/>

### `Client`

We used `Material-UI` as a UI library, `Ricos-Viewer` as our text viewer and `Material-UI/Dropzone` for file uploading.
The client side can be seen as four parts:<br/>

`The App`

This component is the main layout page displaying the toolbar and current page content.<br/>

`Components`

The components are ones used throughout the project, such as the `Tab` and the `Modal`.<br/>

`Text Viewer`

The text viewer uses Ricos - an open source text editing library by Wix.<br/>
This allows us to display all of the content of the demo in a nice way.

`Upload Section`

This section is the core of the demo, the part that connects with the server and makes use of the Algorithms we have implemented.
