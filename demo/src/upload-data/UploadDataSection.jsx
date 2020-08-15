import React, { Component } from "react";
import {
  ButtonGroup,
  Button,
  CircularProgress,
  Paper,
  Typography,
} from "@material-ui/core";

import Upload from "./Upload";
import CustomizeParameters from "./CustomizeParameters";
import { FilesViewer, createFileContent } from "./FilesViewer";
import styles from "./Upload.module.css";

const serverURL = "http://localhost:5000";

export default class UploadDataSection extends Component {
  constructor(props) {
    super(props);
    this.state = {
      proccessing: false,
      isCustomizing: false,
      URLParams: {},
      filesContent: [],
    };
  }

  onActionChosen = (path) => {
    const { URLParams } = this.state;
    let url = new URL(serverURL + path);
    Object.keys(URLParams).forEach((key) =>
      url.searchParams.append(key, URLParams[key])
    );
    this.setState({ proccessing: true }, () => {
      fetch(url, {
        method: "GET",
      }).then((response) => {
        const fileContent = createFileContent(response.url);
        this.setState({
          proccessing: false,
          filesContent: [...this.state.filesContent, fileContent],
        });
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
          lsm to CSV
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
          coordination to csv
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
          lsm to graphs
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
          coordination to graphs
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
    const fileContent = createFileContent(
      serverURL + "/files/" + filename,
      filename
    );
    this.setState({
      proccessing: false,
      filename,
      filesContent: [...this.state.filesContent, fileContent],
    });
  };

  startUploading = () => this.setState({ proccessing: true });

  onParamsUpdate = (URLParams) => {
    this.setState({ isCustomizing: false, URLParams });
  };

  render() {
    return (
      <div className={styles.container}>
        <Paper variant={"outlined"} square>
          <Paper
            className={styles.section}
            variant={"elevation"}
            elevation={10}
          >
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
              Customise Parameters
            </Button>
          </Paper>
          <Paper className={styles.section} variant={"elevation"} elevation={5}>
            <Typography variant={"h6"} color={"primary"}>
              Export Proccessed Data
            </Typography>
            {this.renderConfirmButtons()}
          </Paper>
          {this.onActionProccessing()}
          <CustomizeParameters
            onClose={this.onParamsUpdate}
            isOpen={this.state.isCustomizing}
          />
        </Paper>
        <FilesViewer filesContent={this.state.filesContent} />
      </div>
    );
  }
}
