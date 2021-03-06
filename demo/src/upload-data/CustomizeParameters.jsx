import React, { Component } from "react";
import PropTypes from "prop-types";
import {
  Radio,
  RadioGroup,
  FormControlLabel,
  FormControl,
  TextField,
} from "@material-ui/core";

import { SettingsModal } from "../Components";

export default class CustomizeParameters extends Component {
  constructor(props) {
    super(props);
    this.state = {
      resolution: "BySession",
      eventSpeaker: "",
      measures: [],
      speakers: [],
      transcription: "",
      dyad: "",
      key: "",
      numOfWords: "",
    };
  }

  convertListToString = (list) => {
    let result = "";
    list.forEach((item) => (result += item + " "));
    return result;
  };

  renderParametersForm = () => {
    return (
      <FormControl>
        <TextField
          label="Transcription Key"
          id="transcription-hard-key"
          defaultValue={this.state.key}
          margin="normal"
          onChange={(event) => this.setState({ key: event.target.value })}
        />
        <TextField
          label="Event Speaker"
          id="event-speaker"
          defaultValue={this.state.eventSpeaker}
          margin="normal"
          onChange={(event) =>
            this.setState({ eventSpeaker: event.target.value })
          }
        />
        <TextField
          label="Measures"
          id="measuers"
          defaultValue={this.convertListToString(this.state.measures)}
          margin="normal"
          onChange={(event) =>
            this.setState({ measures: event.target.value.split(" ") })
          }
        />
        <TextField
          label="Speakers"
          id="speakers"
          defaultValue={this.convertListToString(this.state.speakers)}
          margin="normal"
          onChange={(event) =>
            this.setState({ speakers: event.target.value.split(" ") })
          }
        />
        <TextField
          label="Number of words"
          id="num-of-words"
          defaultValue={this.state.numOfWords}
          margin="normal"
          onChange={(event) =>
            this.setState({ numOfWords: event.target.value })
          }
        />
        <RadioGroup
          name={"Conversation Resolution"}
          onChange={(event) =>
            this.setState({ resolution: event.target.value })
          }
          defaultValue={this.state.resolution}
        >
          <FormControlLabel
            value={"BySession"}
            control={<Radio />}
            label={"By Session"}
          />
          <FormControlLabel
            value={"ByDyad"}
            control={<Radio />}
            label={"By Dyad"}
          />
        </RadioGroup>
        <TextField
          label="Dyad Column"
          id="by-dyad"
          defaultValue={this.state.dyad}
          margin="normal"
          onChange={(event) => this.setState({ dyad: event.target.value })}
        />
        {
          <TextField
            label="Session Column"
            id="by-session"
            defaultValue={this.state.transcription}
            margin="normal"
            onChange={(event) =>
              this.setState({ transcription: event.target.value })
            }
            disabled={this.state.resolution !== "BySession"}
          />
        }
      </FormControl>
    );
  };

  onClose() {
    const {
      eventSpeaker,
      measures,
      transcription,
      dyad,
      resolution,
      speakers,
      key,
      numOfWords,
    } = this.state;
    const URLParams = Object.assign(
      {},
      eventSpeaker !== "" && { eventSpeaker },
      resolution === "BySession" && transcription !== "" && { transcription },
      dyad !== "" && { dyad },
      key !== "" && { key },
      numOfWords !== "" && { numOfWords },
      measures.length !== 0 && { measures },
      speakers.length === 2 && { speakers }
    );
    this.props.onClose(URLParams);
  }

  render() {
    return (
      <SettingsModal
        isOpen={this.props.isOpen}
        onClose={() => this.onClose()}
        title={"Data Parameters"}
      >
        {this.renderParametersForm()}
      </SettingsModal>
    );
  }
}

CustomizeParameters.propTypes = {
  isOpen: PropTypes.bool.isRequired,
  onClose: PropTypes.func.isRequired,
};
