import React, { Component } from "react";
import { Button } from "@material-ui/core";
import { DropzoneDialog } from "material-ui-dropzone";
import PropTypes from "prop-types";

export default class Upload extends Component {
  constructor(props) {
    super(props);
    this.state = { open: false };
  }
  handleFileUpload = (files) => {
    const { startUploading, setFilename } = this.props;
    const data = new FormData();
    data.append("file", files[0]);
    startUploading && startUploading();
    fetch("/upload", {
      method: "POST",
      body: data,
    }).then((response) => {
      response.text().then((filename) => setFilename(filename));
    });
    this.setState({ open: false });
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

Upload.propTypes = {
  startUploading: PropTypes.func,
  setFilename: PropTypes.func.isRequired,
};
