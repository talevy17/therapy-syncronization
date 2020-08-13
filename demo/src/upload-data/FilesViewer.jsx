import React from "react";
import { RicosViewer, empty } from "../text-viewer";
import update from "immutability-helper";
import styles from "./file-viewer.module.scss";

export function createFileContent(url, filename) {
  let entityMap = Object.assign({}, empty.entityMap);
  let data = { url };
  if (filename) {
    data.name = filename;
    const fileNameParts = filename.split(".");
    data.type = fileNameParts[fileNameParts.length - 1];
  }
  entityMap = update(entityMap, {
    "0": { data: { $merge: data } },
  });
  return update(empty, { entityMap: { $merge: entityMap } });
}

export function FilesViewer(props) {
  return (
    <div className={styles.container}>
      {props.filesContent.map((content, index) => {
        return (
          <div key={index}>
            <RicosViewer contentState={content} />
          </div>
        );
      })}
    </div>
  );
}
