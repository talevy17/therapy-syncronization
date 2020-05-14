import React, { PureComponent } from "react";
import { Upload } from "./upload-data";
import TabPanel from "./TabPanel";
import { RicosViewer, intro, algorithms, results } from "./text-viewer";
import AppBar from "@material-ui/core/AppBar";
import Tabs from "@material-ui/core/Tabs";
import Tab from "@material-ui/core/Tab";
import "./App.css";

class App extends PureComponent {
  constructor(props) {
    super(props);
    this.state = { tabIndex: 0 };
  }

  a11yProps = (index) => {
    return {
      id: `tab-${index}`,
      "aria-controls": `tabpanel-${index}`,
    };
  };

  render() {
    const { tabIndex } = this.state;
    return (
      <div className={"App"}>
        <AppBar position="static">
          <Tabs
            value={tabIndex}
            onChange={(event, newValue) =>
              this.setState({ tabIndex: newValue })
            }
            aria-label="app-bar-tabs"
            centered
          >
            <Tab label="Intro" {...this.a11yProps(0)} />
            <Tab label="Algorithms" {...this.a11yProps(1)} />
            <Tab label="Our Results" {...this.a11yProps(2)} />
            <Tab label="Upload your own data" {...this.a11yProps(3)} />
          </Tabs>
        </AppBar>
        <TabPanel value={tabIndex} index={0}>
          <RicosViewer contentState={intro} />
        </TabPanel>
        <TabPanel value={tabIndex} index={1}>
          <RicosViewer contentState={algorithms} />
        </TabPanel>
        <TabPanel value={tabIndex} index={2}>
          <RicosViewer contentState={results} />
        </TabPanel>
        <TabPanel value={tabIndex} index={3}>
          <Upload />
        </TabPanel>
      </div>
    );
  }
}

export default App;
