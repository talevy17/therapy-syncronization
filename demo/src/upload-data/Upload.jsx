import React, { Component } from "react";
import { Button, CircularProgress, Paper } from "@material-ui/core";
import { DropzoneDialog } from "material-ui-dropzone";
import "./Upload.scss";

export default class Upload extends Component {
  constructor(props) {
    super(props);
    this.state = { open: false };
  }
  handleFileUpload = (files) => {
    const data = new FormData();
    data.append("file", files[0]);
    this.props.startUploading();
    fetch("/upload", {
      method: "POST",
      body: data,
    }).then((response) => {
      response.text().then((filename) => this.props.setFilename(filename));
    });
    this.setState({ open: false });
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
      <>
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
          submitButtonText={"Upload"}
          onClose={() => this.setState({ open: false })}
          acceptedFiles={[".csv", ".xlsx", ".xls", ".xlsm", ".xlsb"]}
          maxFileSize={500000000}
        />
      </>
    );
  }
}
