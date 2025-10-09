// biome-ignore-all format: DO NOT UPDATE this @generated file

export type ExtensionDataPackageProfile = Package
export type Resource = Table1Resource | Table2Resource

export interface Package {
  $schema: "https://raw.githubusercontent.com/datisthq/extensiondp/v0.1.1/extension/profile.json"
  /**
   * @minItems 1
   */
  resources: [Resource, ...Resource[]]
}
/**
 * Data records have to conform to the Table1 schema
 */
export interface Table1Resource {
  name: "table1"
  schema: "https://raw.githubusercontent.com/datisthq/extensiondp/v0.1.1/extension/schemas/table1.json"
}
/**
 * Data items have to conform to the Table2 schema
 */
export interface Table2Resource {
  name: "table2"
  schema: "https://raw.githubusercontent.com/datisthq/extensiondp/v0.1.1/extension/schemas/table2.json"
}
