import React, { PureComponent } from "react";
import { TabPanel } from "./Components";
import { RicosViewer, intro, algorithms, results } from "./text-viewer";
import UploadDataTab from "./UploadDataTab";
import AppBar from "@material-ui/core/AppBar";
import Tabs from "@material-ui/core/Tabs";
import Tab from "@material-ui/core/Tab";
import styles from "./App.module.css";

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
      <div className={styles.App}>
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
          <UploadDataTab />
        </TabPanel>
      </div>
    );
  }
}

export default App;
