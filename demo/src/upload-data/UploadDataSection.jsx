import React, { Component } from "react";
import {
  ButtonGroup,
  Button,
  CircularProgress,
  Paper,
} from "@material-ui/core";

import Upload from "./Upload";
import CustomizeParameters from "./CustomizeParameters";
import styles from "./Upload.module.css";

export default class UploadDataSection extends Component {
  constructor(props) {
    super(props);
    this.state = {
      proccessing: false,
      isCustomizing: false,
      URLParams: {
        eventSpeaker: "event_speaker",
        measures: [],
        speakers: [],
        session: "session_number",
        dyad: "dyad",
      },
    };
  }

  onActionChosen = (path) => {
    const { URLParams } = this.state;
    let url = new URL("http://localhost:5000" + path);
    Object.keys(URLParams).forEach((key) =>
      url.searchParams.append(key, URLParams[key])
    );
    this.setState({ proccessing: true }, () => {
      fetch(url, {
        method: "GET",
      }).then((response) => {
        this.setState({ proccessing: false });
        window.location.href = response.url;
      });
    });
  };

  renderConfirmButtons = () => {
    const disabled =
      this.state && (!this.state.filename || this.state.proccessing);
    return (
      <ButtonGroup>
        <Button
          onClick={() =>
            this.onActionChosen("/lsm-table/" + this.state.filename)
          }
          variant="contained"
          color="primary"
          component="span"
          disabled={disabled}
        >
          Export lsm to CSV
        </Button>
        <Button
          onClick={() =>
            this.onActionChosen("/coor-table/" + this.state.filename)
          }
          variant="contained"
          color="primary"
          component="span"
          disabled={disabled}
        >
          Export coordination to csv
        </Button>
        <Button
          onClick={() =>
            this.onActionChosen("/lsm-graph/" + this.state.filename)
          }
          variant="contained"
          color="primary"
          component="span"
          disabled={disabled}
        >
          Export lsm to graphs
        </Button>
        <Button
          onClick={() =>
            this.onActionChosen("/coor-graph/" + this.state.filename)
          }
          variant="contained"
          color="primary"
          component="span"
          disabled={disabled}
        >
          Export coordination to graphs
        </Button>
      </ButtonGroup>
    );
  };

  onActionProccessing = () => {
    return this.state && this.state.proccessing ? (
      <div className={styles.progress_container}>
        <CircularProgress className={styles.progress_loader} />
      </div>
    ) : null;
  };

  setFilename = (filename) => {
    console.log(filename);
    this.setState({ proccessing: false, filename });
  };

  startUploading = () => this.setState({ proccessing: true });

  onParamsUpdate = (URLParams) => {
    console.log(URLParams);
    this.setState({ isCustomizing: false, URLParams });
  };

  render() {
    return (
      <Paper className={styles.container} variant={"outlined"} square>
        <Paper className={styles.section} variant={"elevation"} elevation={10}>
          <Upload
            setFilename={this.setFilename}
            startUploading={this.startUploading}
          />
          <Button
            onClick={() => this.setState({ isCustomizing: true })}
            variant="contained"
            color="primary"
            component="span"
          >
            Customize Parameters
          </Button>
        </Paper>
        <Paper className={styles.section} variant={"elevation"} elevation={5}>
          {this.renderConfirmButtons()}
        </Paper>
        {this.onActionProccessing()}
        <CustomizeParameters
          onClose={this.onParamsUpdate}
          isOpen={this.state.isCustomizing}
        />
      </Paper>
    );
  }
}