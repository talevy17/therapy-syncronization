import React, { Component } from "react";
import {
  ButtonGroup,
  Button,
  CircularProgress,
  Paper,
} from "@material-ui/core";
import { DropzoneDialog } from "material-ui-dropzone";
import "./Upload.scss";

export default class Upload extends Component {
  constructor(props) {
    super(props);
    this.state = { open: false, proccessing: false };
  }
  handleFileUpload = (files) => {
    const data = new FormData();
    data.append("file", files[0]);

    fetch("/upload", {
      method: "POST",
      body: data,
    }).then((response) => {
      response
        .text()
        .then((filename) => this.setState({ proccessing: false, filename }));
    });
    this.setState({ proccessing: true, open: false });
  };

  onActionChosen = (path) => {
    this.setState({ proccessing: true }, () => {
      fetch(path, {
        method: "GET",
      }).then((response) => {
        this.setState({ proccessing: false });
        window.location.href = response.url;
      });
    });
  };

  renderButtons = () => {
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
      <div className={"progress-container"}>
        <CircularProgress className={"progress-loader"} />
      </div>
    ) : null;
  };

  render() {
    return (
      <Paper className={"container"} variant={"outlined"} square>
        <Paper className={"section"} variant={"elevation"} elevation={10}>
          <Button
            onClick={() => this.setState({ open: true })}
            variant="contained"
            color="primary"
            component="span"
          >
            Upload
          </Button>
          <DropzoneDialog
            open={this.state.open}
            onSave={this.handleFileUpload}
            cancelButtonText={"Cancel"}
            submitButtonText={"Uplaod"}
            onClose={() => this.setState({ open: false })}
            acceptedFiles={[".csv", ".xlsx", ".xls", ".xlsm", ".xlsb"]}
            maxFileSize={500000000}
          />
        </Paper>
        <Paper className={"section"} variant={"elevation"} elevation={5}>
          {this.renderButtons()}
        </Paper>
        {this.onActionProccessing()}
      </Paper>
    );
  }
}
