CREATE TABLE Presidency_Data.tbl_periphepaltype (
  pertype_id INT NOT NULL PRIMARY KEY IDENTITY(1,1),
  pertype_name VARCHAR(120) NOT NULL,
  pertype_description VARCHAR(200) NOT NULL,
  pertype_is_valid BIT NOT NULL DEFAULT 1,
  pertype_created_at DATETIME NOT NULL DEFAULT GETDATE(),
  pertype_updated_at DATETIME NOT NULL DEFAULT GETDATE(),
  pertype_deleted_at DATETIME NULL,
  pertype_creator_id INT NULL,
  pertype_updater_id INT NULL,
  pertype_deleter_id INT NULL
)
;

GO
CREATE TABLE Presidency_Data.tbl_periphepal (
  per_id INT NOT NULL PRIMARY KEY IDENTITY(1,1),
  per_name VARCHAR(100) NOT NULL,
  per_description VARCHAR(200)  NULL,
  per_type_periphepal_id INT NOT NULL FOREIGN KEY REFERENCES Presidency_Data.tbl_periphepaltype(pertype_id),
  per_is_valid BIT NOT NULL DEFAULT 1,
  per_created_at DATETIME NOT NULL DEFAULT GETDATE(),
  per_updated_at DATETIME NOT NULL DEFAULT GETDATE(),
  per_deleted_at DATETIME NULL,
  per_creator_id INT NULL,
  per_updater_id INT NULL,
  per_deleter_id INT NULL
)
;

GO
CREATE TABLE Presidency_Data.tbl_camera (
  cam_id INT NOT NULL PRIMARY KEY IDENTITY(1,1),
  cam_name VARCHAR(100) NOT NULL,
  cam_is_valid BIT NOT NULL DEFAULT 1,
  cam_created_at DATETIME NOT NULL DEFAULT GETDATE(),
  cam_updated_at DATETIME NOT NULL DEFAULT GETDATE(),
  cam_deleted_at DATETIME NULL,
  cam_creator_id INT NULL,
  cam_updater_id INT NULL,
  cam_deleter_id INT NULL
)
;

GO
CREATE TABLE Presidency_Data.tbl_cameraperiphepal (
  camper_id INT NOT NULL PRIMARY KEY IDENTITY(1,1),
  camper_camera_id INT NOT NULL FOREIGN KEY REFERENCES Presidency_Data.tbl_camera(cam_id),
  camper_periphepal_id INT NOT NULL FOREIGN KEY REFERENCES Presidency_Data.tbl_periphepal(per_id),
  camper_is_valid BIT NOT NULL DEFAULT 1,
  camper_created_at DATETIME NOT NULL DEFAULT GETDATE(),
  camper_updated_at DATETIME NOT NULL DEFAULT GETDATE(),
  camper_deleted_at DATETIME NULL,
  camper_creator_id INT NULL,
  camper_updater_id INT NULL,
  camper_deleter_id INT NULL
)
;

GO
