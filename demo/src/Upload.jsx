import React, { Component } from "react";

export default class Upload extends Component {
  constructor(props) {
    super(props);
    this.state = { upload: false };
  }
  handleFileUpload = (e) => {
    e.preventDefault();

    const data = new FormData();
    data.append("file", this.uploadInput.files[0]);
    this.setState({ upload: true });
    fetch("/upload", {
      method: "POST",
      body: data,
    }).then((response) => {
      this.setState(
        { upload: false },
        () => (window.location.href = response.url)
      );
    });
  };

  renderFileReady = () => {
    return this.state && this.state.upload ? (
      <div> Proccessing Request... </div>
    ) : null;
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
        {this.renderFileReady()}
      </div>
    );
  }
}
