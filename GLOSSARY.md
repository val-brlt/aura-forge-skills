# Aura Forge Project AI

Business vocabulary for persistent functional scoping and software delivery. Preserve the approved historical V1 baseline and distinguish the global MVP from software releases.

## Language

**Project** (*FR : Projet*):
A software initiative described by an initial idea and developed through successive versions.
_Avoid_: Repository (a repository is not the project itself).

**Version** (*FR : Version*):
A software state identified by `MAJOR.MINOR.PATCH`, independently of the global MVP. Historical IDs such as `v1` retain their documentation identity without an inferred software version. Approval of a scope does not establish delivery.
_Avoid_: Phase, session (neither identifies a release).

**Scoping** (*FR : Cadrage fonctionnel*):
The clarification and agreement of functional needs, rules and boundaries for a global MVP or an evolution, without requiring release assignment. The historical V1 application design attaches scoping to a project version; adapting that behavior requires an explicit decision.
_Avoid_: Implementation planning (scoping does not define development tasks).

**MVP** (*FR : Objectif MVP*):
The global indispensable functional objective and its success criteria. It may be delivered through several releases. Its achievement does not automatically establish the first stable version.
_Avoid_: V1, first release (neither is an equivalent of the MVP).

**Functional Scope** (*FR : Périmètre fonctionnel*):
An identified set of agreed needs for the MVP or an evolution. Membership and approval are independent of release assignment. Historical version scopes remain attributable to their original baseline.
_Avoid_: Release plan (it assigns delivery work rather than defining the need).

**Release** (*FR : Release logicielle*):
The actual delivery of an identified software version. A proposed or planned release does not establish shipment; delivered contents remain immutable.
_Avoid_: Approved scope (approval does not release software).

**Milestone** (*FR : Jalon*):
A functional or delivery objective with success criteria and evidence of achievement. The MVP milestone is distinct from software stability.
_Avoid_: Version number (a number does not establish achievement).

**Module** (*FR : Module*):
A coherent functional grouping of a project's features.
_Avoid_: Technical component (modules in this context group user capabilities).

**Feature** (*FR : Fonctionnalité*):
An identifiable functional capability of a project whose agreed behavior can evolve across versions while retaining its identity.
_Avoid_: Task (a task is work toward a capability).

**Proposal** (*FR : Proposition*):
A candidate requirement or decision submitted for the user's consideration, without approval implied by its existence.
_Avoid_: Approved requirement (approval requires an explicit user decision).

**Approval** (*FR : Validation*):
The user's explicit acceptance of an identified proposal or scoping result.
_Avoid_: Delivery (acceptance of a scope is not evidence of a release).

**Delivery** (*FR : Livraison*):
The confirmed release of a project version, distinct from approval of its functional scope.
_Avoid_: Scoping approval (it establishes agreement rather than release).

**Backlog** (*FR : Éléments reportés*):
The single living index of work outside the selected functional change: approved features in another scope, deferred needs, proposals, unresolved decisions and rejected items, each retaining its actual state and original scope. Being outside a change does not remove a feature from its approved MVP.
_Avoid_: Next version scope (deferred work is not automatically selected).

**Scoping Baseline** (*FR : Référence de cadrage*):
The previously approved scope used as context for preparing another version, together with its separately confirmed delivery information.
_Avoid_: Delivered behavior (an approved scope may describe work that has not been released).
