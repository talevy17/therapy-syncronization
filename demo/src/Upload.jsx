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
      this.setState({ uploading: false, url: response.url });
    });
  };

  renderFileReady = () => {
    if (!this.state || (!this.state.url && !this.state.uploading)) {
      return null;
    }
    if (this.state.uploding) {
      return <div> Proccessing Data...</div>;
    }
    if (this.state.url) {
      return (
        <div>
          <button onClick={() => (window.location.href = this.state.url)}>
            Export to CSV
          </button>
          <button> Export graphs </button>
        </div>
      );
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
        {this.renderFileReady()}
      </div>
    );
  }
}
