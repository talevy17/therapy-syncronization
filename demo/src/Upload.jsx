import React, { Component } from "react";

export default class Upload extends Component {
  constructor(props) {
    super(props);
    this.state = { uploading: false };
  }
  handleFileUpload = (e) => {
    e.preventDefault();
    this.setState({ uploading: true });
    const data = new FormData();
    data.append("file", this.uploadInput.files[0]);

    fetch("/upload", {
      method: "POST",
      body: data,
    }).then((response) => {
      response
        .text()
        .then((filename) => this.setState({ uploading: false, filename }));
    });
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

  onFileUploaded = () => {
    if (!this.state || (!this.state.url && !this.state.uploading)) {
      return null;
    }
    if (this.state.uploding) {
      return <div> Uploading...</div>;
    }
    if (this.state.filename) {
      if (this.state.proccessing) {
        return <div> Proccessing Request...</div>;
      } else {
        return (
          <div>
            <button
              onClick={() =>
                this.onActionChosen("/lsm-table/" + this.state.filename)
              }
            >
              Export lsm to CSV
            </button>
            <button
              onClick={() =>
                this.onActionChosen("/coor-table/" + this.state.filename)
              }
            >
              Export coordination to csv
            </button>
            <button
              onClick={() =>
                this.onActionChosen("/lsm-graph/" + this.state.filename)
              }
            >
              Export lsm to graphs
            </button>
            <button
              onClick={() =>
                this.onActionChosen("/coor-graph/" + this.state.filename)
              }
            >
              Export coordination to graphs
            </button>
          </div>
        );
      }
    }
  };

  render() {
    return (
      <div>
        <form onSubmit={this.handleFileUpload}>
          <div>
            <input
              ref={(ref) => {
                this.uploadInput = ref;
              }}
              type="file"
            />
          </div>
          <div>
            <button>Upload</button>
          </div>
        </form>
        {this.onFileUploaded()}
      </div>
    );
  }
}
