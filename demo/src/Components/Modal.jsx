import React, { Component } from "react";
import {
  Modal,
  Typography,
  IconButton,
  Button,
  Paper,
} from "@material-ui/core";

import closeIcon from "./closeIcon";

import "./modal.scss";

export default function SettingsModal(props) {
  const { isOpen, modalBody, onClose, title } = props;
  return (
    <Modal
      className={"modal-container"}
      open={isOpen}
      onClose={() => onClose()}
    >
      <Paper>
        <IconButton className={"close-button"} onClick={() => onClose()}>
          {closeIcon()}
        </IconButton>
        <Paper className={"settings-container"}>
          <Typography variant={"h3"} color={"primary"}>
            {title}
          </Typography>
          {modalBody()}
        </Paper>
      </Paper>
    </Modal>
  );
}
