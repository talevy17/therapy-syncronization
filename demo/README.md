## Quick Start

To run the demo locally make sure you have Python3 and npm or yarn installed.<br />

### First Run

<ol> 
<li> Open a terminal window and go in the directory `therapy-syncronization/demo` </li>
<li> Run `npm i` or `yarn install` to install all of the dependencies </li>
<li> Run `npm run start` to run the Client App</li>
<li> Open another terminal window in the same directory and run `npm run start-server` to start the Server </li>
</ol>

### Adding a new Tab

Simply create the component you want to be rendered in a new tab, let's call it `Component` <br />
Then, in `App.js` add a `Tab` component with a `label` prop to best describe the tab and call `{...this.a11yProps(i)}` with `i` the new tab index. <br />
lastly, add a `TabPanel` component with `Component` as it's child <br />
You`re all set.

### Updating or Writting new text content

Here https://github.com/talevy17/therapy-syncronization/tree/master/demo/src/text-viewer/fixtures you'll find JSON files which are feeded as `ContentState` by props to `RicosViewer` our choice of rich-text library. <br />
To update content or write a new one you can use `RicosEditor` by either implementing a simple one https://wix-incubator.github.io/rich-content/docs/ricos/quick-start/
or just use this surge: wix-rich-content.herokuapp.com/, write whatever you like and copy the JSON from the `ContentState` tab.

### Adding a new algorithm

On the client side it's easy - once you've got the algorithm implemented and a new endpoint in the `api` https://github.com/talevy17/therapy-syncronization/tree/master/api, just add a new button in `upload-data/UploadDataSection.jsx` with the relative URL to the endpoint and a file name/

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

We used `Material-UI` as a UI library, `Ricos-Viewer` as our text viewer and `Material-UI/Dropzone` for file uploading.<br/>
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

### `Server`

The server was written with `Flask` creating endpoints and configuration to allow a user to upload data and use our tools. <br/>
See more in https://github.com/talevy17/therapy-syncronization/tree/master/api
