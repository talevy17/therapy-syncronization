import React from "react";
import PropTypes from "prop-types";
import { Modal, Typography, IconButton, Paper } from "@material-ui/core";

import closeIcon from "./closeIcon";

import styles from "./modal.module.css";

export default function SettingsModal(props) {
  const { isOpen, children, onClose, title } = props;
  return (
    <Modal
      className={styles.modal_container}
      open={isOpen}
      onClose={() => onClose()}
    >
      <Paper>
        <IconButton className={styles.close_button} onClick={() => onClose()}>
          {closeIcon()}
        </IconButton>
        <Paper className={styles.settings_container}>
          {title && (
            <Typography variant={"h3"} color={"primary"}>
              {title}
            </Typography>
          )}
          {children}
        </Paper>
      </Paper>
    </Modal>
  );
}

SettingsModal.propTypes = {
  isOpen: PropTypes.bool.isRequired,
  onClose: PropTypes.func.isRequired,
  title: PropTypes.string,
  children: PropTypes.any,
};
